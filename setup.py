import textwrap

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="email_domain_verification",
        description="Can Verify All The Email Forms And Domains",
        author="Mahdi Niknejad",
        author_email="mmahdiniknejad@gmail.com",
        url="https://github.com/khodnevis-app/development_tools",
        project_urls={
            "Documentation": "https://github.com/khodnevis-app/development_tools",
            "Source": "https://github.com/khodnevis-app/development_tools",
            "Tracker": "https://github.com/khodnevis-app/development_tools/issues",
        },
        long_description=textwrap.dedent(""""""),
        packages=["email_domain_verification"],
        package_data={"email_domain_verification": ["py.typed", "*.pyi"]},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Software Development",
        ],
        python_requires=">=3.10",
        install_requires=[
            "requests",
        ],
    )
