FROM python:3-bullseye

RUN apt-get -y update
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH /root/.cargo/bin:$PATH

WORKDIR /tmp
COPY apt-packages-list.txt /tmp/apt-packages-list.txt
RUN xargs -a apt-packages-list.txt apt-get install -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "agent_kernel.py"]