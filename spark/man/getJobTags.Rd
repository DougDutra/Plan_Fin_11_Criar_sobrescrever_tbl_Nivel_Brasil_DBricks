% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/sparkR.R
\name{getJobTags}
\alias{getJobTags}
\title{Get the tags that are currently set to be assigned to all the jobs started by this thread.}
\usage{
getJobTags()
}
\description{
Get the tags that are currently set to be assigned to all the jobs started by this thread.
}
\note{
getJobTags since 3.5.0
}
\examples{
\dontrun{
sparkR.session()
tags <- getJobTags()
}
}
