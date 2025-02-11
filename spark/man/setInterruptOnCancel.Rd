% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/sparkR.R
\name{setInterruptOnCancel}
\alias{setInterruptOnCancel}
\title{Set the behavior of job cancellation from jobs started in this thread.}
\usage{
setInterruptOnCancel(interruptOnCancel)
}
\arguments{
\item{interruptOnCancel}{If true, then job cancellation will result in `Thread.interrupt()`
being called on the job's executor threads. This is useful to help ensure that the tasks
are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS
may respond to Thread.interrupt() by marking nodes as dead.}
}
\description{
Set the behavior of job cancellation from jobs started in this thread.
}
\note{
cancelJobGroup since 3.5.0
}
\examples{
\dontrun{
sparkR.session()
setInterruptOnCancel(true)
}
}
