package main

import (
	"fmt"
	"os"
	"runtime"

	"github.com/go-gl/gl/v4.1-core/gl"
	"github.com/go-gl/glfw/v3.3/glfw"

	imgui "github.com/inkyblackness/imgui-go/v4"
)

var (
	g_window    *glfw.Window
	g_wndWidth  int = 1152
	g_wndHeight int = 864
)

func keyCallback(w *glfw.Window, key glfw.Key, scancode int, action glfw.Action, mods glfw.ModifierKey) {
	if key == glfw.KeyEscape {
		w.SetShouldClose(true)
	}

	if key == glfw.KeyQ {
		fmt.Println("Q is pressed!")
	}
}

func initGlfwWindow() {
	if err := glfw.Init(); err != nil {
		panic(err)
	}

	glfw.WindowHint(glfw.ContextVersionMajor, 4)
	glfw.WindowHint(glfw.ContextVersionMinor, 1)
	glfw.WindowHint(glfw.Resizable, glfw.False)
	// glfw.WindowHint(glfw.DoubleBuffer, glfw.True)
	// glfw.WindowHint(glfw.OpenGLProfile, glfw.OpenGLCoreProfile)
	// glfw.WindowHint(glfw.OpenGLForwardCompatible, glfw.True)

	wnd, err := glfw.CreateWindow(g_wndWidth, g_wndHeight, "Conway's Game of Life", nil, nil)
	g_window = wnd
	if err != nil {
		panic(err)
	}

	g_window.MakeContextCurrent()

	if err := gl.Init(); err != nil {
		panic(err)
	}

	g_window.SetKeyCallback(keyCallback)
}

func setOglDefaults() {
	gl.Viewport(0, 0, int32(g_wndWidth), int32(g_wndHeight))
	gl.ClearColor(0.0, 0.0, 0.0, 0.0)
}

func initImGui() {
	ctx := imgui.CreateContext(nil)

	io := imgui.CurrentIO()

	platform, err := platforms.NewGLFW(io, platforms.GLFWClientAPIOpenGL3)
	if err != nil {
		_, _ = fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(-1)
	}
}

func loop() {
	for !g_window.ShouldClose() {
		glfw.PollEvents()

		g_window.SwapBuffers()
	}
}

func main() {
	runtime.LockOSThread()

	initGlfwWindow()

	initImGui()

	setOglDefaults()

	loop()
}
