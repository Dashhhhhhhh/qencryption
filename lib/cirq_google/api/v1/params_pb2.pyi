"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ParameterSweep(google.protobuf.message.Message):
    """Specifies how to repeatedly sample a circuit, with or without sweeping over
    varying parameter-dicts.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REPETITIONS_FIELD_NUMBER: builtins.int
    SWEEP_FIELD_NUMBER: builtins.int
    repetitions: builtins.int
    """How many times to sample, for each parameter-dict that is swept over.
    This must be set to a value strictly greater than zero.
    """
    @property
    def sweep(self) -> global___ProductSweep:
        """Which parameters, that control gates in the circuit, to try.

        The keys of the parameters generated by this sweep must be a superset
        of the keys in the program's operations.  When this is not specified,
        no parameterization is assumed (and the program must have no
        ParameterizedFloat's with keys.
        """
    def __init__(
        self,
        *,
        repetitions: builtins.int = ...,
        sweep: global___ProductSweep | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sweep", b"sweep"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["repetitions", b"repetitions", "sweep", b"sweep"]) -> None: ...

global___ParameterSweep = ParameterSweep

@typing_extensions.final
class ProductSweep(google.protobuf.message.Message):
    """A cartesian product of parameter sweeps."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FACTORS_FIELD_NUMBER: builtins.int
    @property
    def factors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ZipSweep]:
        """A list of parameter sweeps to combine into a cartesian sweep.

        Example: if one of the factors assigns
        "a": 0.0
        "a": 1.0
        and another assigns
        "b": 2.0
        "b": 3.0
        then the product of these assigns
        "a": 0.0, "b": 2.0
        "a": 0.0, "b": 3.0
        "a": 1.0, "b": 2.0
        "a": 1.0, "b": 3.0
        """
    def __init__(
        self,
        *,
        factors: collections.abc.Iterable[global___ZipSweep] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["factors", b"factors"]) -> None: ...

global___ProductSweep = ProductSweep

@typing_extensions.final
class ZipSweep(google.protobuf.message.Message):
    """A pairwise-joining of parameter sweeps."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SWEEPS_FIELD_NUMBER: builtins.int
    @property
    def sweeps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SingleSweep]:
        """Note: if one sweep is shorter, the others will be truncated.

        Example: if one of the factors assigns
        "a": 0.0
        "a": 1.0
        and another assigns
        "b": 2.0
        "b": 3.0
        then the product of these assigns
        "a": 0.0, "b": 2.0
        "a": 1.0, "b": 3.0
        """
    def __init__(
        self,
        *,
        sweeps: collections.abc.Iterable[global___SingleSweep] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sweeps", b"sweeps"]) -> None: ...

global___ZipSweep = ZipSweep

@typing_extensions.final
class SingleSweep(google.protobuf.message.Message):
    """A set of values to try for a particular parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMETER_KEY_FIELD_NUMBER: builtins.int
    POINTS_FIELD_NUMBER: builtins.int
    LINSPACE_FIELD_NUMBER: builtins.int
    parameter_key: builtins.str
    """The parameter key being varied. This cannot be the empty string."""
    @property
    def points(self) -> global___Points:
        """An explicit list of points to try."""
    @property
    def linspace(self) -> global___Linspace:
        """Uniformly-spaced sampling over a range."""
    def __init__(
        self,
        *,
        parameter_key: builtins.str = ...,
        points: global___Points | None = ...,
        linspace: global___Linspace | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["linspace", b"linspace", "points", b"points", "sweep", b"sweep"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["linspace", b"linspace", "parameter_key", b"parameter_key", "points", b"points", "sweep", b"sweep"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["sweep", b"sweep"]) -> typing_extensions.Literal["points", "linspace"] | None: ...

global___SingleSweep = SingleSweep

@typing_extensions.final
class Points(google.protobuf.message.Message):
    """A list of explicit values."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POINTS_FIELD_NUMBER: builtins.int
    @property
    def points(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """The values."""
    def __init__(
        self,
        *,
        points: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["points", b"points"]) -> None: ...

global___Points = Points

@typing_extensions.final
class Linspace(google.protobuf.message.Message):
    """A range of evenly-spaced values.

    Example: if the first_point is 1.0, the last_point is 2.0 ,
    and the num_points is 5, thi corresponds to the points
      1.0, 1.25, 1.5, 1.75, 2.0
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIRST_POINT_FIELD_NUMBER: builtins.int
    LAST_POINT_FIELD_NUMBER: builtins.int
    NUM_POINTS_FIELD_NUMBER: builtins.int
    first_point: builtins.float
    """The start of the range."""
    last_point: builtins.float
    """The end of the range."""
    num_points: builtins.int
    """The number of points in the range (including first and last). Must be
    greater than zero. If it is 1, the first_point and last_point must be
    the same.
    """
    def __init__(
        self,
        *,
        first_point: builtins.float = ...,
        last_point: builtins.float = ...,
        num_points: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["first_point", b"first_point", "last_point", b"last_point", "num_points", b"num_points"]) -> None: ...

global___Linspace = Linspace

@typing_extensions.final
class ParameterDict(google.protobuf.message.Message):
    """A point sampled during a parameter sweep."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AssignmentsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.float
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.float = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ASSIGNMENTS_FIELD_NUMBER: builtins.int
    @property
    def assignments(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.float]:
        """Maps parameter names to values."""
    def __init__(
        self,
        *,
        assignments: collections.abc.Mapping[builtins.str, builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assignments", b"assignments"]) -> None: ...

global___ParameterDict = ParameterDict