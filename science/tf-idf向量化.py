import jieba
from gensim import corpora
from gensim.models import TfidfModel

# 定义函数，创建停用词列表
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
# 定义函数，对sentences中的每个元素进行分词去停用词
def seg_sentence(sentences):
    stopwords = stopwordslist("stopwords.txt")  
    cut_word = []
    cut_words = []
    for sentence in sentences:
        sentence_seged = jieba.lcut(sentence)       
        for word in sentence_seged:
            if word not in stopwords: 
                if word != ' ':
                    cut_word.append(word)
        cut_words.append(cut_word)
        cut_word = []    
    return cut_words

# 定义文本数据
sentences = [
    "通过挖掘大规模文本数据，我们可以发现隐藏在文本信息中的宝藏。",
    "文本中蕴含着丰富的知识，通过对文本进行分析和挖掘，可以获取这些知识。",
    "通过对文本进行挖掘，我们还可以从大量的文本中提取出有用的知识。"
]

# 载入jieba自定义词典
jieba.load_userdict("userdict.txt")
# 调用分词去停用词函数
tokenized_sentences = seg_sentence(sentences)

# 构建词表
dictionary = corpora.Dictionary(tokenized_sentences)
# 计算词频（Term Frequency）
corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_sentences]
# 构建TF-IDF模型
tfidf_model = TfidfModel(corpus)
# 计算每个句子的TF-IDF向量表示
tfidf_vectors = [tfidf_model[corpus[i]] for i in range(len(corpus))]

# 输出词表
print("词表：", dictionary.token2id)
# 输出结果：原始文本、每个文本的TF-IDF向量表示
range_num = len(sentences)
for i in range(range_num):
    print("原始文本：", sentences[i])
    print("TF-IDF向量表示",)
    print(tfidf_vectors[i])