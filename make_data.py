import json
import os
from datasets import load_dataset

# 1. 设置保存路径 (会自动在你的根目录下创建 data/conll03)
output_dir = "./data/conll03"
os.makedirs(output_dir, exist_ok=True)

# 2. 下载数据
print("正在下载 CoNLL-2003 数据...")
# 如果网络不好，可能需要魔法，或者手动下载数据集
dataset = load_dataset("conll2003", trust_remote_code=True)

# 3. 标签映射 (CoNLL的标准标签)
id2label = {
    0: "O", 1: "PER", 2: "PER", 3: "ORG", 4: "ORG", 
    5: "LOC", 6: "LOC", 7: "MISC", 8: "MISC"
}

def convert_to_binder_json(data_split, filename):
    file_path = os.path.join(output_dir, filename)
    print(f"正在生成: {file_path}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data_split:
            tokens = item['tokens']
            ner_tags = item['ner_tags']
            
            entities = []
            i = 0
            while i < len(ner_tags):
                tag = ner_tags[i]
                if tag == 0: 
                    i += 1
                    continue
                
                label = id2label[tag]
                start = i
                i += 1
                
                # 寻找实体结束位置
                while i < len(ner_tags) and ner_tags[i] != 0 and id2label[ner_tags[i]] == label:
                    if ner_tags[i] in [1, 3, 5, 7]: # 遇到新的B-tag
                        break
                    i += 1
                end = i - 1
                
                # Binder代码需要的格式通常是 [start, end, label]
                entities.append({"start": start, "end": end, "label": label})
            
            # 写入一行 JSON
            f.write(json.dumps({"sentence": tokens, "ner": entities}) + "\n")

# 4. 执行
convert_to_binder_json(dataset['train'], 'train.json')
convert_to_binder_json(dataset['validation'], 'dev.json')
convert_to_binder_json(dataset['test'], 'test.json')
print("✅ 数据准备完成！")