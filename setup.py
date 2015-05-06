#!/usr/bin/env python

from setuptools import setup

setup(name='ceph-release-notes',
      version='0.1',
      install_requires=[
          'githubpy',
          'GitPython',
      ],
      scripts=['ceph_release_notes'],
      )
