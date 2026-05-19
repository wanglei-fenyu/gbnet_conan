# gbnet_conan
游戏网络库 基本组件，使用conan管理依赖
# gbnet - Game Network Library

[![Conan Version](https://img.shields.io/badge/conan-0.1.0-blue)](https://conan.io)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![C++](https://img.shields.io/badge/C++-20-blue)](https://isocpp.org/)

一个简单的 C++ 游戏网络编程库，基于 Boost.Asio，支持 SSL、Zlib 压缩和 Protobuf 序列化。

## ✨ 特性

- 🚀 基于 Boost.Asio 的高性能网络通信
- 🔒 可选的 OpenSSL 加密支持
- 📦 可选的 Zlib 压缩支持
- 📡 可选的 Protobuf 序列化支持
- 🎯 跨平台（Windows/Linux/macOS）
- 📦 Conan 包管理支持

## 📋 系统要求

- CMake 3.15+
- C++20 编译器（MSVC 2019+ / GCC 11+ / Clang 14+）
- Conan 2.x

## 🔧 安装

### 方式一：使用 Conan（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/wanglei-fenyu/gbnet_conan.git
cd gbnet

# 2. 创建 Conan 包
conan create . --build=missing

# 3. 在你的项目中使用
# 在 conanfile.txt 中添加: gbnet/0.1.0
