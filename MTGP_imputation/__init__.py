# -*- coding: utf-8 -*-

#2016/7/18 Packages for imputation of missing data with MTGP in 'Multi-task Gaussian process for imputing missing data in multi-trait and multi-environment trials'

#This package is designed for python2. It does not work for python3.

#This packages requires additional packages as below..
#numpy
#scipy
#pandas
#scikit-tensor

#This package is devided into three parts: "mktensor", "mkkernel" and "MTGP".
#"mktensor" makes tensor array data, which is necessary for calculation from csvs.
#"mkkernel" is designed for making kernel matrix.
#"MTGP" conducts imputation and parameter search for kernel by cross validation.

