> **oepkgs社区软件包引入各版本分支原则：**
- 1. 软件包引入master保护分支，通过对应sig组maintainer或者对应源码仓committer review、approve即可。
- 2. 软件包引入到oepkgs其他保护分支，需根据valid_release_branch，通过对应sig组的maintainer或者对应源码仓committer review、approve即可。

> **oepkgs仓库**

- extras
  oepkgs主仓，仓库中的软件包大部分取自其他仓库，以保证用户只需要添加这一个仓库，便能获取到其他所有仓库中大部分的软件包，受限于软件包多版本现状，无法覆盖所有的软件包，一部分extras仓库中无法获取的软件包，可到其他仓库中查找

- compatible
  通过拉取来自其他 Linux 发行版仓库中的源码包，在 openEuler 上重新编译构建，并在 openEuler 上通过了安装测试的软件包，compatible 仓库中 c6，c7，c8，f33，f34，f35，f36，rawhide 分别表示软件源码包来源是 centos6，centos7，centos8，fedora33，fedora34，fedora35，fedora36，fedora-rawhide，不同来源可以用来区分软件包的版本号，来源是 centos8 的软件包一般而言能拿到较高版本的软件包

- contrib
  来自许多开发者贡献的软件包，contrib 仓库下以软件包类别划分出仓库名，显然，bigdata 仓库中是大数据场景下需要应用的软件包。


> **valid_release_branch:**

- extras 仓库管控

| 分支名 | 解释 |
|---|---|
| master | 用于管控 oepkgs 主仓 openEuler-20.03-LTS-SP1/extras 下软件包的引入 |
| openEuler-20.03-LTS-SP1 | 用于管控 oepkgs 主仓 openEuler-20.03-LTS-SP1/extras 下软件包的引入 |
| openEuler-20.03-LTS-SP3 | 用于管控 oepkgs 主仓 openEuler-20.03-LTS-SP3/extras 下软件包的引入 |
| openEuler-22.03-LTS | 用于管控 oepkgs 主仓 openEuler-22.03-LTS/extras 下软件包的引入 |

- compatible 仓库管控：

| 分支名 | 解释 |
|---|---|
| compatible_c7_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs compatible 仓 openEuler-20.03-LTS-SP3/compatible/c7 下软件包的引入 |
| compatible_c8_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs compatible 仓 openEuler-20.03-LTS-SP3/compatible/c8 下软件包的引入 |
| compatible_f35_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs compatible 仓 openEuler-20.03-LTS-SP3/compatible/f35 下软件包的引入 |

- contrib 仓库管控：

| 分支名 | 解释 |
|---|---|
| contrib_bigdata_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/bigdata 下软件包的引入 |
| contrib_bigdata_openEuler-20.03-LTS-SP1 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP1/contrib/bigdata 下软件包的引入 |
| contrib_virtual_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/virtual 下软件包的引入 |
| contrib_basic-system_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/basic-system 下软件包的引入 |

- contrib multi_version 仓库管控（openstack 有 Queens、Rocky、Wallaby 等多版本的软件包引入）

| 分支名 | 解释 |
|---|---|
| Muti-Version_openstack-wallaby_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/openstack/wallaby 下软件包的引入 |
| Muti-Version_openstack-rocky_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/openstack/rocky 下软件包的引入 |
| Muti-Version_openstack-queens_openEuler-20.03-LTS-SP3 | 用于管控 oepkgs contrib 仓 openEuler-20.03-LTS-SP3/contrib/openstack/queens 下软件包的引入 |