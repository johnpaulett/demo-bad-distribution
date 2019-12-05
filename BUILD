load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@pip_deps//:requirements.bzl", "all_requirements")


py_binary(
    name = "local",
    srcs = [
        "sample.py",
    ],
    deps = all_requirements,
    main = "sample.py",
)

py3_image(
    name = "docker",
    srcs = [
        "sample.py",
    ],
    deps = all_requirements,
    main = "sample.py",
)