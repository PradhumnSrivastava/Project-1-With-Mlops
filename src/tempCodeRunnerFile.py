if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)