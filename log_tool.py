import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Log filtering tool")
    parser.add_argument("--level", type=str, help="INFO, WARN, ERROR (case-insensitive)")
    parser.add_argument("--service", type=str, help="Service name (case-sensitive)")
    parser.add_argument("--out", type=str, default="filtered_logs.txt", help="Output file")
    return parser.parse_args()

def is_valid_line(parts):
    # Must have exactly 4 parts
    if len(parts) != 4:
        return False

    level = parts[1].strip().upper()
    return level in ["INFO", "WARN", "ERROR"]

def main():
    args = parse_args()

    # Normalize level filter if provided
    level_filter = args.level.upper() if args.level else None
    service_filter = args.service

    valid_lines = []
    total_valid = 0
    written = 0

    # Read file
    with open("logs.txt", "r") as f:
        for raw in f:
            line = raw.strip()
            parts = [p.strip() for p in line.split("|")]

            if not is_valid_line(parts):
                continue  # ignore invalid

            total_valid += 1

            timestamp, level, service, message = parts
            level = level.upper()

            # Filtering
            if level_filter and level != level_filter:
                continue
            if service_filter and service != service_filter:
                continue

            valid_lines.append(f"{timestamp} | {level} | {service} | {message}")

    # Write output
    with open(args.out, "w") as out_file:
        for l in valid_lines:
            out_file.write(l + "\n")
            written += 1

    # Print summary
    print(f"Valid lines scanned: {total_valid}")
    print(f"Lines written: {written}")
    print(f"Output file: {args.out}")

if __name__ == "__main__":
    main()