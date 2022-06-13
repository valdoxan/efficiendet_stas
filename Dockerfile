FROM bingliunpu/pytorch1.8.1-py38-cuda11.1-cudnn8-ubuntu18.04

COPY ./efficientdet_for_aicup ./

RUN pip install -r requirements.txt