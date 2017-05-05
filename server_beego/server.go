package main

import (
	"fmt"
	"workshop"

	"github.com/astaxie/beego"
	"github.com/astaxie/beego/context"
)

// Run the world
func main() {

	beego.Get("/", func(ctx *context.Context) {
		sum := workshop.MySum(1, 2)
		ctx.Output.Body([]byte(fmt.Sprintf("hello world! the sum is %d", int(sum))))
	})

	beego.Run()
}
