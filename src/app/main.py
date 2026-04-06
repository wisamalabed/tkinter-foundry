"""Main application entry point."""

import tkinter as tk
from app.views.main_window import MainWindow
from app.controllers.main_controller import MainController


def main() -> None:
    """Initialize and run the tkinter application."""
    root = tk.Tk()
    root.title("Tkinter App")
    root.geometry("800x600")
    
    # Set minimum window size
    root.minsize(400, 300)
    
    # Configure style
    configure_styles(root)
    
    # Create MVC components
    controller = MainController(root)
    view = MainWindow(root, controller)
    
    # Start the application
    root.mainloop()


def configure_styles(root: tk.Tk) -> None:
    """Configure application styles and themes."""
    # Configure root style
    root.configure(bg="#f0f0f0")
    
    # Configure ttk styles
    style = tk.ttk.Style()
    style.theme_use('clam')
    
    # Custom styles
    style.configure('Title.TLabel', 
                   font=('Arial', 16, 'bold'),
                   background='#f0f0f0')
    
    style.configure('Header.TLabel',
                   font=('Arial', 12, 'bold'),
                   background='#f0f0f0')


if __name__ == "__main__":
    main()
