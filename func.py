from parliament import Context, event
import logging
import sys

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)  # Write to stdout
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@event
def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    # Add your business logic here

    # The return value here will be applied as the data attribute
    # of a CloudEvent returned to the function invoker
    ce = context.cloud_event
    inc_data = ce.data
    logger.info("Received CE " + str(ce))

    out_data = {
        "comment": inc_data["CONTENT"],
        "video": inc_data["VIDEO_NAME"],
        "date": inc_data["DATE"],
        "prev-source": ce["source"]
    }
    logger.info("Sending " + str(out_data))
    return out_data