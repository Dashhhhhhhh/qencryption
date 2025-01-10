from . cimport sf_error
cdef void _set_action(sf_error.sf_error_t, sf_error.sf_action_t) noexcept nogil
cdef void *_export_beta_pdf_float
cdef void *_export_beta_pdf_double
cdef void *_export_beta_ppf_float
cdef void *_export_beta_ppf_double
cdef void *_export_binom_cdf_float
cdef void *_export_binom_cdf_double
cdef void *_export_binom_isf_float
cdef void *_export_binom_isf_double
cdef void *_export_binom_pmf_float
cdef void *_export_binom_pmf_double
cdef void *_export_binom_ppf_float
cdef void *_export_binom_ppf_double
cdef void *_export_binom_sf_float
cdef void *_export_binom_sf_double
cdef void *_export_cauchy_isf_float
cdef void *_export_cauchy_isf_double
cdef void *_export_cauchy_ppf_float
cdef void *_export_cauchy_ppf_double
cdef void *_export_hypergeom_cdf_float
cdef void *_export_hypergeom_cdf_double
cdef void *_export_hypergeom_mean_float
cdef void *_export_hypergeom_mean_double
cdef void *_export_hypergeom_pmf_float
cdef void *_export_hypergeom_pmf_double
cdef void *_export_hypergeom_sf_float
cdef void *_export_hypergeom_sf_double
cdef void *_export_hypergeom_skewness_float
cdef void *_export_hypergeom_skewness_double
cdef void *_export_hypergeom_variance_float
cdef void *_export_hypergeom_variance_double
cdef void *_export_invgauss_isf_float
cdef void *_export_invgauss_isf_double
cdef void *_export_invgauss_ppf_float
cdef void *_export_invgauss_ppf_double
cdef void *_export_landau_cdf_float
cdef void *_export_landau_cdf_double
cdef void *_export_landau_isf_float
cdef void *_export_landau_isf_double
cdef void *_export_landau_pdf_float
cdef void *_export_landau_pdf_double
cdef void *_export_landau_ppf_float
cdef void *_export_landau_ppf_double
cdef void *_export_landau_sf_float
cdef void *_export_landau_sf_double
cdef void *_export_nbinom_cdf_float
cdef void *_export_nbinom_cdf_double
cdef void *_export_nbinom_isf_float
cdef void *_export_nbinom_isf_double
cdef void *_export_nbinom_kurtosis_excess_float
cdef void *_export_nbinom_kurtosis_excess_double
cdef void *_export_nbinom_mean_float
cdef void *_export_nbinom_mean_double
cdef void *_export_nbinom_pmf_float
cdef void *_export_nbinom_pmf_double
cdef void *_export_nbinom_ppf_float
cdef void *_export_nbinom_ppf_double
cdef void *_export_nbinom_sf_float
cdef void *_export_nbinom_sf_double
cdef void *_export_nbinom_skewness_float
cdef void *_export_nbinom_skewness_double
cdef void *_export_nbinom_variance_float
cdef void *_export_nbinom_variance_double
cdef void *_export_ncf_isf_float
cdef void *_export_ncf_isf_double
cdef void *_export_ncf_kurtosis_excess_float
cdef void *_export_ncf_kurtosis_excess_double
cdef void *_export_ncf_mean_float
cdef void *_export_ncf_mean_double
cdef void *_export_ncf_pdf_float
cdef void *_export_ncf_pdf_double
cdef void *_export_ncf_sf_float
cdef void *_export_ncf_sf_double
cdef void *_export_ncf_skewness_float
cdef void *_export_ncf_skewness_double
cdef void *_export_ncf_variance_float
cdef void *_export_ncf_variance_double
cdef void *_export_nct_isf_float
cdef void *_export_nct_isf_double
cdef void *_export_nct_kurtosis_excess_float
cdef void *_export_nct_kurtosis_excess_double
cdef void *_export_nct_mean_float
cdef void *_export_nct_mean_double
cdef void *_export_nct_pdf_float
cdef void *_export_nct_pdf_double
cdef void *_export_nct_ppf_float
cdef void *_export_nct_ppf_double
cdef void *_export_nct_sf_float
cdef void *_export_nct_sf_double
cdef void *_export_nct_skewness_float
cdef void *_export_nct_skewness_double
cdef void *_export_nct_variance_float
cdef void *_export_nct_variance_double
cdef void *_export_ncx2_cdf_float
cdef void *_export_ncx2_cdf_double
cdef void *_export_ncx2_isf_float
cdef void *_export_ncx2_isf_double
cdef void *_export_ncx2_pdf_float
cdef void *_export_ncx2_pdf_double
cdef void *_export_ncx2_ppf_float
cdef void *_export_ncx2_ppf_double
cdef void *_export_ncx2_sf_float
cdef void *_export_ncx2_sf_double
cdef void *_export_skewnorm_cdf_float
cdef void *_export_skewnorm_cdf_double
cdef void *_export_skewnorm_isf_float
cdef void *_export_skewnorm_isf_double
cdef void *_export_skewnorm_ppf_float
cdef void *_export_skewnorm_ppf_double
cdef void *_export__stirling2_inexact
cdef void *_export_ibeta_float
cdef void *_export_ibeta_double
cdef void *_export_ibetac_float
cdef void *_export_ibetac_double
cdef void *_export_ibetac_inv_float
cdef void *_export_ibetac_inv_double
cdef void *_export_ibeta_inv_float
cdef void *_export_ibeta_inv_double
cdef void *_export_faddeeva_dawsn
cdef void *_export_faddeeva_dawsn_complex
cdef void *_export_fellint_RC
cdef void *_export_cellint_RC
cdef void *_export_fellint_RD
cdef void *_export_cellint_RD
cdef void *_export_fellint_RF
cdef void *_export_cellint_RF
cdef void *_export_fellint_RG
cdef void *_export_cellint_RG
cdef void *_export_fellint_RJ
cdef void *_export_cellint_RJ
cdef void *_export_faddeeva_erf
cdef void *_export_faddeeva_erfc_complex
cdef void *_export_faddeeva_erfcx
cdef void *_export_faddeeva_erfcx_complex
cdef void *_export_faddeeva_erfi
cdef void *_export_faddeeva_erfi_complex
cdef void *_export_erfinv_float
cdef void *_export_erfinv_double
cdef void *_export_hyp1f1_double
cdef void *_export_faddeeva_log_ndtr
cdef void *_export_faddeeva_log_ndtr_complex
cdef void *_export_ncf_cdf_float
cdef void *_export_ncf_cdf_double
cdef void *_export_ncf_ppf_float
cdef void *_export_ncf_ppf_double
cdef void *_export_nct_cdf_float
cdef void *_export_nct_cdf_double
cdef void *_export_faddeeva_ndtr
cdef void *_export_powm1_float
cdef void *_export_powm1_double
cdef void *_export_faddeeva_voigt_profile
cdef void *_export_faddeeva_w
cdef void *_export_wrightomega
cdef void *_export_wrightomega_real