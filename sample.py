try:
    import grpc
    print('Success')
except ImportError as e:
    print('Failed')

    import os

    print(os.listdir('/app/docker.binary.runfiles/pip_deps_pypi__grpcio_1_25_0/grpc/_cython'))
    print('')
    raise e
