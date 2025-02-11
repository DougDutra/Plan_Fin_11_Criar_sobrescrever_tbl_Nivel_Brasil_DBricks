% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/catalog.R
\name{functionExists}
\alias{functionExists}
\title{Checks if the function with the specified name exists.}
\usage{
functionExists(functionName)
}
\arguments{
\item{functionName}{name of the function, allowed to be qualified with catalog name}
}
\description{
Checks if the function with the specified name exists.
}
\note{
since 3.4.0
}
\examples{
\dontrun{
sparkR.session()
functionExists("spark_catalog.default.myFunc")
}
}
