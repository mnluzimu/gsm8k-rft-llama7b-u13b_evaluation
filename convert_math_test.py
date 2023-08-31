import json

def main():
    with open("MATH_test_orig.jsonl", "r") as f:
        datas = [json.loads(line) for line in f]
    prefix_len = len("Solve the problem and put your answer in '\\boxed{}'. \n")
    new_datas = [{"id": data["id"], "question": data["text"][0][prefix_len:], "answer": data["answer"]} for data in datas]
    with open("MATH_test.jsonl", "w") as f:
        for new_data in new_datas:
            f.write(json.dumps(new_data) + "\n")

if __name__ == "__main__":
    main()