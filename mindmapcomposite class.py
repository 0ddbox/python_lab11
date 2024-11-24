# mindmap_composite.py

class MindMapComposite:
    def __init__(self, name, shape):
        """Initialize a composite node with a name, shape, and empty children list."""
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        """Add a child node to this composite."""
        self.children.append(child)

    def remove(self, child):
        """Remove a child node from this composite."""
        self.children.remove(child)

    def __str__(self):
        """Return string representation using the shape template."""
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        """Display this node and all its children with proper indentation."""
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        """Return the template string for the given shape."""
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{{}}}}}}",
            "bang": ")){}((",
            "plain": "{}"
        }
        return shapes.get(self.shape, "{}")