% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/catalog.R
\name{listCatalogs}
\alias{listCatalogs}
\title{Returns a list of catalog available}
\usage{
listCatalogs()
}
\value{
a SparkDataFrame of the list of catalog.
}
\description{
Returns a list of catalog available.
}
\note{
since 3.4.0
}
\examples{
\dontrun{
sparkR.session()
listCatalogs()
}
}
