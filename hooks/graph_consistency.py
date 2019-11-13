def pre_export(output, conanfile, conanfile_path, reference, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))


def post_export(output, conanfile, conanfile_path, reference, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))


def pre_source(output, conanfile, conanfile_path, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))


def post_source(output, conanfile, conanfile_path, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))


def pre_build(output, conanfile, **kwargs):
    assert conanfile
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))
        output.info("package_id=%s" % kwargs["package_id"])
    else:
        output.info("conanfile_path=%s" % kwargs["conanfile_path"])


def post_build(output, conanfile, **kwargs):
    assert conanfile
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))
        output.info("package_id=%s" % kwargs["package_id"])
    else:
        output.info("conanfile_path=%s" % kwargs["conanfile_path"])


def pre_package(output, conanfile, conanfile_path, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))
        output.info("package_id=%s" % kwargs["package_id"])


def post_package(output, conanfile, conanfile_path, **kwargs):
    assert conanfile
    output.info("conanfile_path=%s" % conanfile_path)
    if conanfile.in_local_cache:
        output.info("reference=%s" % str(kwargs["reference"]))
        output.info("package_id=%s" % kwargs["package_id"])


def pre_upload(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def post_upload(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def pre_upload_recipe(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def post_upload_recipe(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def pre_upload_package(output, conanfile_path, reference, package_id, remote,
                       **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("package_id=%s" % package_id)
    output.info("remote.name=%s" % remote.name)


def post_upload_package(output, conanfile_path, reference, package_id, remote,
                        **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("package_id=%s" % package_id)
    output.info("remote.name=%s" % remote.name)


def pre_download(output, reference, remote, **kwargs):
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def post_download(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def pre_download_recipe(output, reference, remote, **kwargs):
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def post_download_recipe(output, conanfile_path, reference, remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("remote.name=%s" % remote.name)


def pre_download_package(output, conanfile_path, reference, package_id, remote,
                         **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("package_id=%s" % package_id)
    output.info("remote.name=%s" % remote.name)


def post_download_package(output, conanfile_path, reference, package_id,
                          remote, **kwargs):
    output.info("conanfile_path=%s" % conanfile_path)
    output.info("reference=%s" % str(reference))
    output.info("package_id=%s" % package_id)
    output.info("remote.name=%s" % remote.name)


def pre_package_info(output, conanfile, reference, **kwargs):
    output.info("reference=%s" % reference.full_repr())
    output.info("conanfile.cpp_info.defines=%s" % conanfile.cpp_info.defines)


def post_package_info(output, conanfile, reference, **kwargs):
    output.info("reference=%s" % reference.full_repr())
    output.info("conanfile.cpp_info.defines=%s" % conanfile.cpp_info.defines)