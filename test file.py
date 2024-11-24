# test_mindmap_leaf.py
from mindmap_leaf import MindMapLeaf


def test_leaf():
    leaf = MindMapLeaf("Jean-Luc Picard", "circle")
    print("Testing MindMapLeaf str():", str(leaf))  # Should display "((Jean-Luc Picard))"
    print("Testing MindMapLeaf display() with indent 2:")
    leaf.display(2)  # Should display "  ((Jean-Luc Picard))"

    # Test different shapes
    shapes = ["oval", "square", "cloud", "hexagon", "bang", "plain"]
    print("\nTesting different shapes:")
    for shape in shapes:
        leaf = MindMapLeaf("Test", shape)
        print(f"{shape}: {str(leaf)}")


print("Running MindMapLeaf tests...")
test_leaf()
print("MindMapLeaf tests completed!")

# test_mindmap_composite.py
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite


def test_composite():
    root = MindMapComposite("Root", "circle")
    leaf1 = MindMapLeaf("Child 1", "square")
    leaf2 = MindMapLeaf("Child 2", "cloud")

    print("Testing add() method:")
    root.add(leaf1)
    root.add(leaf2)

    print("\nTesting str():", str(root))  # Should display "((Root))"

    print("\nTesting display() with hierarchy:")
    root.display()

    print("\nTesting remove() method:")
    root.remove(leaf1)
    root.display()


print("Running MindMapComposite tests...")
test_composite()
print("MindMapComposite tests completed!")