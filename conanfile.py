from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, rmdir
from conan.tools.scm import Git
import os

class gbnetConan(ConanFile):
    name = "gbnet"
    version = "0.1.0"
    author = "leo"

    description = "A simple C++ library for game network programming"
    url = "https://github.com/wanglei-fenyu/gbnet_conan"
    license = "MIT"

    # 设置和选项
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],      # 动态库还是静态库
        "fPIC": [True, False],        # 位置无关代码（Linux 静态库需要）
        "with_ssl": [True, False],    # 可选：是否启用 SSL
        "with_zlib": [True, False],
        "with_protobuf": [True, False],
    }

    default_options = {
        "shared": False,              # 默认静态库
        "fPIC": True,
        "with_ssl": True,
        "with_zlib": True,
        "with_protobuf": True,
    }

    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        # 示例：依赖 Boost.Asio（网络核心）
        self.requires("boost/1.90.0")
    
        if self.options.with_ssl:
            self.requires("openssl/3.0.13")
    
        if self.options.with_zlib:
            self.requires("zlib/1.3.1")

        self.requires("protobuf/3.21.12")
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC  # Windows 不需要 fPIC


    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        
        tc = CMakeToolchain(self)
        tc.variables["GBNET_WITH_SSL"] = self.options.with_ssl
        tc.variables["GBNET_WITH_ZLIB"] = self.options.with_zlib  
        tc.variables["GBNET_WITH_PROTOBUF"] = self.options.with_protobuf
        tc.variables["CMAKE_CXX_STANDARD"] = "20"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        

    def package_info(self):
        self.cpp_info.libs = ["gbnet"]
        self.cpp_info.includedirs = ["include"]
        
        if self.settings.os == "Linux":
            self.cpp_info.system_libs.append("pthread")

        requires_list = ["boost::boost"]

        if self.options.with_ssl:
            requires_list.append("openssl::openssl")
        if self.options.with_zlib:
            requires_list.append("zlib::zlib")
        if self.options.with_protobuf:
            requires_list.append("protobuf::libprotobuf")   