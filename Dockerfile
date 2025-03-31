# docker login ; docker build -f Dockerfile -t mquinson/infosansordi ; docker push

FROM alpine:latest
RUN apk add --no-cache typst mdbook pipx py3-markdown texlive texmf-dist-langfrench texmf-dist-latexextra make
RUN pipx install --global linkchecker
