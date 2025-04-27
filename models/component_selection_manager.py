class ComponentSelectionManager:
    def __init__(self):
        # Store selected component names
        self.selected_components = {
            "CPU": None,
            "GPU": None,
            "HDD": [],  # Changed to a list to handle multiple HDD selections
            "Motherboard": None,
            "PSU": None,
            "RAM": [],  # List to handle multiple RAM selections
            "SSD": [],  # List to handle multiple SSD selections
            "Monitor": None,
            "CPU_Cooler": None,
            "Case": None
        }

    def set_component_name(self, component_type, component_name):
        """Set the selected Name for a specific component type."""
        if component_type in self.selected_components:
            if component_type in ["RAM", "SSD", "HDD"]:  # Handle multiple selections
                self.selected_components[component_type].append(component_name)
                print(f"{component_type} added with Name: {component_name}")
            else:
                self.selected_components[component_type] = component_name
                print(f"{component_type} selected with Name: {component_name}")
        else:
            print(f"Invalid component type: {component_type}")

    def get_component_name(self, component_type):
        """Retrieve the selected Name(s) for a specific component type."""
        if component_type in self.selected_components:
            component_name = self.selected_components[component_type]
            print(f"{component_type} currently selected: {component_name}")
            return component_name
        else:
            print(f"Invalid component type: {component_type}")
            return None

    def get_component_names(self):
        """Retrieve all selected component Names."""
        print("All selected components:", self.selected_components)
        return self.selected_components

    def clear_component(self, component_type):
        """Clear the selection for a specific component type."""
        if component_type in self.selected_components:
            if component_type in ["RAM", "SSD", "HDD"]:  # Clear lists for multiple selections
                self.selected_components[component_type] = []
            else:
                self.selected_components[component_type] = None
            print(f"{component_type} selection cleared.")
        else:
            print(f"Invalid component type: {component_type}")

    def clear_all_components(self):
        """Clear all selected components."""
        for component in self.selected_components:
            if component in ["RAM", "SSD", "HDD"]:  # Clear lists for multiple selections
                self.selected_components[component] = []
            else:
                self.selected_components[component] = None
        print("All component selections cleared.")
