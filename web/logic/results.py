from typing import Optional
from urllib.parse import urlparse

from web.models.result import CORSRequestResult


class ResultManager:
    """Manager class for containing all methods related to the receipt and processing of CORS
    scanning results.
    """

    @staticmethod
    def accept_success(
        host: str,
        fetched_url: str,
        content: str,
        duration: float,
        status_code: int,
        user_agent: Optional[str],
        user_ip: Optional[str],
    ) -> CORSRequestResult:
        """Record that a successful CORS request was observed for the given URL. Return the associated
        database record once created.
        """
        parsed = urlparse(fetched_url)
        result = CORSRequestResult(
            host_domain=host,
            url=fetched_url,
            url_domain=parsed.netloc,
            content=content,
            duration=duration,
            success=True,
            user_agent=user_agent,
            user_ip=user_ip,
            status_code=status_code,
        )
        result.save()
        return result

    @staticmethod
    def accept_failure(
        host: str,
        err_msg: str,
        err_location: str,
        duration: float,
        fetched_url: Optional[str],
        user_agent: Optional[str],
        user_ip: Optional[str],
    ) -> CORSRequestResult:
        """Record that a CORS request failed for the given URL and reason. Return the associated
        database record once created.
        """
        parsed = urlparse(fetched_url)
        result = CORSRequestResult(
            host_domain=host,
            url=fetched_url,
            url_domain=parsed.netloc,
            err_msg=err_msg,
            err_location=err_location,
            duration=duration,
            success=False,
            user_agent=user_agent,
            user_ip=user_ip,
        )
        result.save()
        return result
