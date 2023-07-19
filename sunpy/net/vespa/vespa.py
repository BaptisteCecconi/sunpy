__all__ = ['VESPAClient', 'VESPAResponse']


class JSOCResponse(QueryResponseTable):
    pass


class JSOCClient(BaseClient):
    """
    Provides access to the VESPA services.

    It exposes a similar API to the VSO client, although the underlying model
    is more complex. 

    
    """

    @property
    def info_url(self):
        return 'http://europlanet-vespa.eu'

    def search(self, *query, **kwargs):
        """
        Build a VESPA query and submit it to the VO for processing.

        Takes a variable number of `~sunpy.net.vespa.attrs` as parameters,
        which are chained together using the AND (``&``) operator.

        Complex queries to be easily formed using logical operators such as
        ``&`` and ``|``, in the same way as the VSO client.

        Parameters
        ----------
        *query : a variable number of `~sunpy.net.vespa.attrs`
            as parameters, which are chained together using
            the ``AND`` (``&``) operator.

        Returns
        -------
        response : `~sunpy.net.vespa.vespa.VESPAResponse` object
            A collection of records that the query returns.

        Examples
        --------
        *Example 1*

        Request all ORN/NDA dynamic spectra between 2023-05-21T00:00 and
        2023-05-24T00:00::

            >>> import astropy.units as u
            >>> from sunpy.net import vespa
            >>> from sunpy.net import attrs as a
            >>> client = vespa.VESPAClient()  # doctest: +REMOTE_DATA
            >>> response = client.search(a.Time('2023-05-21T00:00:00', '2023-05-24T00:00:00'),
            ...                          a.jsoc.Series('aia.lev1_euv_12s'), a.Wavelength(304*u.AA),
            ...                          a.jsoc.Segment('image'))  # doctest: +REMOTE_DATA
            >>> print(response)  # doctest: +REMOTE_DATA
                   tmin          instrument_host_name instrument_name WAVELNTH CAR_ROT
            -------------------- -------- -------- -------- -------
            2017-09-06T11:59:59Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:00:11Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:00:23Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:00:35Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:00:47Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:00:59Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:01:11Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:01:23Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:01:35Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:01:47Z  SDO/AIA    AIA_4      304    2194
            2017-09-06T12:01:59Z  SDO/AIA    AIA_4      304    2194



