cmake_minimum_required(VERSION 3.28)
project(gbnet VERSION 1.0.0 LANGUAGES CXX)

if(CMAKE_TOOLCHAIN_FILE)
    include(${CMAKE_TOOLCHAIN_FILE})
endif()

if(DEFINED CONAN_CXX_FLAGS)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${CONAN_CXX_FLAGS}")
endif()


find_package(Boost REQUIRED)

if(GBNET_WITH_SSL)
    find_package(OpenSSL REQUIRED)
endif()

if(GBNET_WITH_ZLIB)
    find_package(ZLIB REQUIRED)
endif()

if(GBNET_WITH_PROTOBUF)
    find_package(Protobuf REQUIRED)
endif()

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB_RECURSE SRC_FILES 
    "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/*.h"
)


message(STATUS "Found ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp and *.h")
message(STATUS "Source files: ${SRC_FILES}")

add_library(gbnet ${SRC_FILES})


target_include_directories(gbnet PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:include>
)

target_link_libraries(gbnet PUBLIC
    Boost::boost
)

if(GBNET_WITH_SSL)
    target_link_libraries(gbnet PUBLIC OpenSSL::SSL OpenSSL::Crypto)
endif()

if(GBNET_WITH_ZLIB)
    target_link_libraries(gbnet PUBLIC ZLIB::ZLIB)
endif()

if(GBNET_WITH_PROTOBUF)
    target_link_libraries(gbnet PUBLIC protobuf::libprotobuf)
endif()

if(NOT BUILD_SHARED_LIBS)
    set_target_properties(gbnet PROPERTIES POSITION_INDEPENDENT_CODE ON)
endif()

# 安装规则
install(TARGETS gbnet
    EXPORT gbnetTargets
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

install(DIRECTORY src/ DESTINATION include/gbnet
    FILES_MATCHING PATTERN "*.h"
)

install(EXPORT gbnetTargets
    FILE gbnetConfig.cmake
    NAMESPACE gbnet::
    DESTINATION lib/cmake/gbnet
)
