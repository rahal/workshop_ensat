FROM golang:1.8.1


RUN go get github.com/smartystreets/goconvey
RUN go get github.com/stretchr/testify/assert
RUN go get github.com/astaxie/beego
RUN go get github.com/beego/bee

