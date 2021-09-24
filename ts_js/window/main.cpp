#include <iostream>
#include <Windows.h>
#include <windowsX.h>

LRESULT CALLBACK WndProc(HWND, UINT, WPARAM,LPARAM);

int APIENTRY WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance,
						LPSTR lpCmdLine,int nCmdShow)
{
	HWND hwnd;
	MSG msg;
	WNDCLASS w;
	
	memset(&w,0,sizeof(WNDCLASS));
	
	w.style = CS_HREDRAW | CS_VREDRAW;
	w.lpfnWndProc = WndProc;
	w.hInstance = hInstance;
	w.hbrBackground = (HBRUSH)GetStockBrush(BLACK_BRUSH);
	w.lpszClassName = "Windows";
	w.cbWndExtra = 0;
	w.cbClsExtra = 0;
	w.hIcon = LoadIcon(NULL,IDI_APPLICATION);
    w.hCursor = LoadCursor(NULL,IDC_NO);
	w.lpszMenuName = NULL;
      	
	RegisterClass(&w);
		
	hwnd = CreateWindow("Windows","Windows", WS_OVERLAPPEDWINDOW,
						10,10,600,480,NULL,NULL,hInstance,NULL);
	
	if (hwnd == 0)
    {
        std::cout << "Error can not create window" << std::endl;
        return 1;
    }
	
	ShowWindow(hwnd,nCmdShow);
	UpdateWindow(hwnd);
	
	while(GetMessage(&msg,NULL,0,0))
	{
		switch(msg.message)
		{
			case WM_KEYDOWN:
				switch (msg.wParam)
				{
					case VK_ESCAPE:
					{
						PostQuitMessage(0);
						return 0;
						break;
					}
				}
		}
		
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	
	return msg.wParam;
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT Message, WPARAM wparam,LPARAM lparam)
{
	PAINTSTRUCT ps;
    HDC hdc;
     
	if (Message == WM_DESTROY )
	{
		switch(Message)
		{
			case WM_CREATE:
			{
				return 0;
				break;
			}
			
			case WM_PAINT:
			{
				hdc = BeginPaint(hwnd,&ps);
				EndPaint(hwnd,&ps);
				return 0;
				break;
			}
			
			case WM_DESTROY:
			{
				PostQuitMessage(0);
				return 0;
				break;
			}
			
			default: break;
		}
		
		PostQuitMessage(0);
		return 0;
	}
	
	return DefWindowProc(hwnd,Message,wparam,lparam);
}

