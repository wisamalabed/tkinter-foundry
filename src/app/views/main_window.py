"""Main application window view."""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.controllers.main_controller import MainController


class MainWindow:
    """Main application window view."""
    
    def __init__(self, root: tk.Tk, controller: 'MainController') -> None:
        """Initialize the main window view.
        
        Args:
            root: The root tkinter window
            controller: The main controller
        """
        self.root = root
        self.controller = controller
        
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the user interface components."""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header = ttk.Label(main_frame, text="Tkinter App", style='Title.TLabel')
        header.pack(pady=(0, 20))
        
        # Content frame
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Example button
        self.example_button = ttk.Button(
            content_frame,
            text="Click Me!",
            command=self.controller.on_button_click
        )
        self.example_button.pack(pady=10)
        
        # Status label
        self.status_label = ttk.Label(
            content_frame,
            text="Ready",
            style='Header.TLabel'
        )
        self.status_label.pack(pady=10)
    
    def update_status(self, message: str) -> None:
        """Update the status label.
        
        Args:
            message: The status message to display
        """
        self.status_label.config(text=message)
