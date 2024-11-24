# mindmap_leaf.py

class MindMapLeaf:
    def __init__(self, name, shape):
        """Initialize a leaf node with a name and shape."""
        self.name = name
        self.shape = shape

    def __str__(self):
        """Return string representation using the shape template."""
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        """Display the leaf node with proper indentation."""
        print(" " * indent + str(self))

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