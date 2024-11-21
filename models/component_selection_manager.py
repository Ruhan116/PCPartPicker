class ComponentSelectionManager:
    def __init__(self):
        # Store selected component names
        self.selected_components = {
            "CPU": None,
            "GPU": None,
            "HDD": None,
            "Motherboard": None,
            "PSU": None,
            "RAM": None,
            "SSD": None,
        }

    def set_component_name(self, component_type, component_name):
        """Set the selected Name for a specific component type."""
        if component_type in self.selected_components:
            self.selected_components[component_type] = component_name
            print(f"{component_type} selected with Name: {component_name}")
        else:
            print(f"Invalid component type: {component_type}")

    def get_component_names(self):
        """Retrieve all selected component Names."""
        return self.selected_components
