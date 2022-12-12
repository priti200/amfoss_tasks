package main

import (
	"syscall/js"
)

var count = 0

func incWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count += 1
		output.Set("innerHTML", count)
		return count
	})
}

func decWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count -= 1
		output.Set("innerHTML", count)
		return count
	})
}

func resetWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count = 0
		output.Set("innerHTML", count)
		return count
	})
}

func main() {
	js.Global().Set("incFunc", incWrapper())
	js.Global().Set("decFunc", decWrapper())
	js.Global().Set("resetFunc", resetWrapper())
	<-make(chan bool)
}
