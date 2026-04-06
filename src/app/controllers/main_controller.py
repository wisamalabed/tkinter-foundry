"""Main application controller."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.views.main_window import MainWindow


class MainController:
    """Main application controller."""
    
    def __init__(self, root: tk.Tk) -> None:
        """Initialize the main controller.
        
        Args:
            root: The root tkinter window
        """
        self.root = root
        self.view = None
    
    def set_view(self, view: 'MainWindow') -> None:
        """Set the view associated with this controller.
        
        Args:
            view: The view to set
        """
        self.view = view
    
    def on_button_click(self) -> None:
        """Handle button click event."""
        if self.view:
            self.view.update_status("Button clicked!")
