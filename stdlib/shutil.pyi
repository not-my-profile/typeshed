import os
import sys
from _typeshed import StrOrBytesPath, StrPath, SupportsRead, SupportsWrite
from typing import Any, AnyStr, Callable, Iterable, NamedTuple, Sequence, TypeVar, Union, overload

__all__ = [
    "copyfileobj",
    "copyfile",
    "copymode",
    "copystat",
    "copy",
    "copy2",
    "copytree",
    "move",
    "rmtree",
    "Error",
    "SpecialFileError",
    "ExecError",
    "make_archive",
    "get_archive_formats",
    "register_archive_format",
    "unregister_archive_format",
    "get_unpack_formats",
    "register_unpack_format",
    "unregister_unpack_format",
    "unpack_archive",
    "ignore_patterns",
    "chown",
    "which",
    "get_terminal_size",
    "SameFileError",
    "disk_usage",
]

# these type variables are used by the functions that return the passed destination
# which can be either a path-like object or a string/bytes
_StrOrBytesPathT = TypeVar("_StrOrBytesPathT", bound=StrOrBytesPath)
_StrPathT = TypeVar("_StrPathT", bound=StrPath)

class Error(OSError): ...
class SameFileError(Error): ...
class SpecialFileError(OSError): ...
class ExecError(OSError): ...
class ReadError(OSError): ...
class RegistryError(Exception): ...

def copyfileobj(fsrc: SupportsRead[AnyStr], fdst: SupportsWrite[AnyStr], length: int = ...) -> None: ...
def copyfile(src: StrOrBytesPath, dst: _StrOrBytesPathT, *, follow_symlinks: bool = ...) -> _StrOrBytesPathT: ...
def copymode(src: StrOrBytesPath, dst: StrOrBytesPath, *, follow_symlinks: bool = ...) -> None: ...
def copystat(src: StrOrBytesPath, dst: StrOrBytesPath, *, follow_symlinks: bool = ...) -> None: ...
def copy(src: StrOrBytesPath, dst: _StrOrBytesPathT, *, follow_symlinks: bool = ...) -> _StrOrBytesPathT: ...
def copy2(src: StrOrBytesPath, dst: _StrOrBytesPathT, *, follow_symlinks: bool = ...) -> _StrOrBytesPathT: ...
def ignore_patterns(*patterns: StrPath) -> Callable[[Any, list[str]], set[str]]: ...

if sys.version_info >= (3, 8):
    def copytree(
        src: StrPath,
        dst: _StrPathT,
        symlinks: bool = ...,
        ignore: None | Callable[[str, list[str]], Iterable[str]] | Callable[[StrPath, list[str]], Iterable[str]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
        dirs_exist_ok: bool = ...,
    ) -> _StrPathT: ...

else:
    def copytree(
        src: StrPath,
        dst: _StrPathT,
        symlinks: bool = ...,
        ignore: None | Callable[[str, list[str]], Iterable[str]] | Callable[[StrPath, list[str]], Iterable[str]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
    ) -> _StrPathT: ...

def rmtree(path: StrOrBytesPath, ignore_errors: bool = ..., onerror: Callable[[Any, Any, Any], Any] | None = ...) -> None: ...

_CopyFn = Union[Callable[[str, str], None], Callable[[StrPath, StrPath], None]]

# N.B. shutil.move appears to take bytes arguments, however,
# this does not work when dst is (or is within) an existing directory.
# (#6832)
if sys.version_info >= (3, 9):
    def move(src: StrPath, dst: _StrPathT, copy_function: _CopyFn = ...) -> _StrPathT: ...

else:
    # See https://bugs.python.org/issue32689
    def move(src: str, dst: _StrPathT, copy_function: _CopyFn = ...) -> _StrPathT: ...

class _ntuple_diskusage(NamedTuple):
    total: int
    used: int
    free: int

def disk_usage(path: int | StrOrBytesPath) -> _ntuple_diskusage: ...
@overload
def chown(path: StrOrBytesPath, user: str | int, group: None = ...) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: None = ..., *, group: str | int) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: None, group: str | int) -> None: ...
@overload
def chown(path: StrOrBytesPath, user: str | int, group: str | int) -> None: ...

if sys.version_info >= (3, 8):
    @overload
    def which(cmd: _StrPathT, mode: int = ..., path: StrPath | None = ...) -> str | _StrPathT | None: ...
    @overload
    def which(cmd: bytes, mode: int = ..., path: StrPath | None = ...) -> bytes | None: ...

else:
    def which(cmd: _StrPathT, mode: int = ..., path: StrPath | None = ...) -> str | _StrPathT | None: ...

def make_archive(
    base_name: str,
    format: str,
    root_dir: StrPath | None = ...,
    base_dir: StrPath | None = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    owner: str | None = ...,
    group: str | None = ...,
    logger: Any | None = ...,
) -> str: ...
def get_archive_formats() -> list[tuple[str, str]]: ...
@overload
def register_archive_format(
    name: str, function: Callable[..., object], extra_args: Sequence[tuple[str, Any] | list[Any]], description: str = ...
) -> None: ...
@overload
def register_archive_format(
    name: str, function: Callable[[str, str], object], extra_args: None = ..., description: str = ...
) -> None: ...
def unregister_archive_format(name: str) -> None: ...

if sys.version_info >= (3, 7):
    def unpack_archive(filename: StrPath, extract_dir: StrPath | None = ..., format: str | None = ...) -> None: ...

else:
    # See http://bugs.python.org/issue30218
    def unpack_archive(filename: str, extract_dir: StrPath | None = ..., format: str | None = ...) -> None: ...

@overload
def register_unpack_format(
    name: str,
    extensions: list[str],
    function: Callable[..., object],
    extra_args: Sequence[tuple[str, Any]],
    description: str = ...,
) -> None: ...
@overload
def register_unpack_format(
    name: str, extensions: list[str], function: Callable[[str, str], object], extra_args: None = ..., description: str = ...
) -> None: ...
def unregister_unpack_format(name: str) -> None: ...
def get_unpack_formats() -> list[tuple[str, list[str], str]]: ...
def get_terminal_size(fallback: tuple[int, int] = ...) -> os.terminal_size: ...
