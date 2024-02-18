
# mapper2D

mapper2D is a Python library for generating 2D height maps.

## Installation

You can install mapper2D using pip:

```
pip install mapper2D
```

## Usage

```
import mapper2D

# Generate a height map
height_map = mapper2D.mapper2D(width=800, ground_mid=400, contrast=2, smoothing_levels=7)
```

## Parameters

- `width`: The width of the height map.
- `ground_mid`: The midpoint of the ground level.
- `contrast`: The contrast of the height map.
- `smoothing_levels`: The number of smoothing levels applied to the height map.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

