# Semantic-Text-Segmentation-docker
Semantic-Text-Segmentation-with-Embeddings docker api



导出依赖
> pipreqs ./ --force

模型下载
https://www.kaggle.com/datasets/terrychanorg/semantic-text-segmentation-model

模型命名为`app/data/word2vec.6B.bin`

构建镜像
> docker build -t napoler/text_segmentation:0.1.2 .
运行镜像
> docker run -d -p 3011:80 napoler/text_segmentation:0.1.2