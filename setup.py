from setuptools import setup, find_packages

setup(
    name='Jonathan-art116',
    version='0.0.2',
    author='Jonathan',
    author_email='xyzning@qq.com',
    long_description='This is a demo of setup, do not install this package.',
    url='https://github.com/Jonathan-art116/systeminfo.git',
    packages = find_packages(),
    classifiers = [
        # 发展时期,常见的如下
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 开发的目标用户
        'Intended Audience :: Developers',

        # 属于什么类型
        'Topic :: Software Development :: Build Tools',

        # 许可证信息
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # 目标 Python 版本
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

     # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/foo 的可执行文件
    # 该文件入口指向 foo/main.py 的main 函数
    # entry_points={
    #     'console_scripts': [
    #         'foo = foo.main:main'
    #     ]
    # },

    # 将 bin/foo.sh 和 bar.py 脚本，生成到系统 PATH中
    # 执行 python setup.py install 后
    # 会生成 如 /usr/bin/foo.sh 和 如 /usr/bin/bar.py
    # scripts=['bin/foo.sh', 'bar.py']


    # 限制python 版本
    # python_requires='>=2.7, <=3',

    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    # install_requires=['docutils>=0.3'],

    # setup.py 本身要依赖的包，这通常是为一些setuptools的插件准备的配置
    # 这里列出的包，不会自动安装。
    # setup_requires=['pbr'],

    # 仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。
    # 在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
    # tests_require=[
    #     'pytest>=3.3.1',
    #     'pytest-cov>=2.5.1',
    # ],

    # 用于安装setup_requires或tests_require里的软件包
    # 这些信息会写入egg的 metadata 信息中
    # dependency_links=[
    #     "http://example2.com/p/foobar-1.0.tar.gz",
    # ],

    # install_requires 在安装模块时会自动安装依赖包
    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    # extras_require={
    #     'PDF':  ["ReportLab>=1.2", "RXP"],
    #     'reST': ["docutils>=0.3"],
    # }


     # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    # data_files=[
    #     ('', ['conf/*.conf']),
    #     ('/usr/lib/systemd/system/', ['bin/*.service']),
    #            ],

    # 希望被打包的文件
    # package_data={
    #     '':['*.txt'],
    #     'bandwidth_reporter':['*.txt']
    #            },
    # 不打包某些文件
    # exclude_package_data={
    #     'bandwidth_reporter':['*.txt']
    #            }
)