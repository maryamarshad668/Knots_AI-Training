import csv
import json

def csv_to_jsonl(csv_path, jsonl_path):
    rows = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    with open(jsonl_path, "w") as f:
        for row in rows:
            entry = {
                "instruction": row["instruction"].strip(),
                "context": row["context"].strip(),
                "response": row["response"].strip()
            }
            f.write(json.dumps(entry) + "\n")
    return len(rows)

def format_for_sft(jsonl_path, formatted_path):
    with open(jsonl_path, "r") as f:
        lines = [json.loads(l) for l in f.readlines()]
    with open(formatted_path, "w") as f:
        for item in lines:
            text = f"### Instruction:\n{item['instruction']}\n\n### Context:\n{item['context']}\n\n### Response:\n{item['response']}"
            f.write(json.dumps({"text": text}) + "\n")

if __name__ == "__main__":
    count = csv_to_jsonl("support_data.csv", "support_data.jsonl")
    format_for_sft("support_data.jsonl", "support_data_sft.jsonl")
    print(f"Converted {count} rows")
    print("Wrote support_data.jsonl and support_data_sft.jsonl")