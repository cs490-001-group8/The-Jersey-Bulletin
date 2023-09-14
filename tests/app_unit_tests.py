"""
    app_unit_tests.py
    This file does all tests for app.py
"""
import unittest
import unittest.mock as mock
from datetime import datetime
import sys
from os.path import dirname, join

# pylint: disable=C0413
sys.path.append(join(dirname(__file__), "../"))

# pylint: disable=R0903
# pylint: disable=W0613
# pylint: disable=C0415
# pylint: disable=W0612
# pylint: disable=E0401
# pylint: disable=C0330
# pylint: disable=E1120
# pylint: disable=R0201

def weather_do_nothing(one, two, three):
    """Do nothing instead of getting weather"""
    return


class MockedThemeObj:
    """Pretend to be a theme object"""

    def __init__(self, name, email, login_type, pattern, value):
        self.name = name
        self.email = email
        self.login_type = login_type
        self.pattern = pattern
        self.value = value


class MockedQueryResponseObj:
    """Pretend to be a query response object"""

    # pylint: disable=R0902
    def __init__(self, text, name, time):
        # pylint: disable=C0103
        self.id = 7
        self.text = text
        self.name = name
        self.time = time
        self.likes = 0
        self.comment_id = 7
        self.pattern = "w"
        self.value = "78"
        self.personal_values = "{'News': True, 'Weather': True, 'Traffic': False, \
            'Bills': False, 'Politician_Twitter': False, \
            'Hiking_Destinations': True, 'Sports': False}"


class MockedOrderResponse:
    """Pretend to be an order response"""

    def __init__(self, texts):
        self.texts = texts

    def all(self):
        """Mock an all() call from a query response"""
        return self.texts


class MockedFilterResponse:
    """Pretend to be an query response"""

    # pylint: disable=R0201

    def __init__(self, texts):
        self.texts = texts
        self.order = MockedOrderResponse(texts)

    def all(self):
        """Mock an all() call from a query response"""
        return self.texts

    def first(self):
        """Mock a first() call from a query response"""
        return self.texts[0]

    def delete(self):
        """Mock a delete() call from a query response"""
        return None

    def order_by(self, arg):
        """Mock an order_by() call from a query response"""
        return self.order


class MockedFilterNoneResponse:
    """Pretend to be an query response"""

    # pylint: disable=R0201

    def __init__(self, texts):
        self.texts = texts

    def first(self):
        """Mock a first() call from a query response"""
        return None


class MockedQueryResponse:
    """Pretend to be an query response"""

    def __init__(self, text):
        self.texts = [MockedQueryResponseObj(text["text"], text["name"], text["time"])]

    def filter(self, text, text2="", text3=""):
        """Pretend to be an query filter"""
        return MockedFilterResponse(self.texts)

    # pylint: disable=C0103
    # pylint: disable=W0622
    def filter_by(self, id="", email="", login_type="", comment_id=0):
        """Pretend to be an query filter"""
        if comment_id == 8:
            return MockedFilterNoneResponse(self.texts)
        return MockedFilterResponse(self.texts)

    def all(self):
        """Mock an all() call from a query response"""
        return self.texts


class MockedRequestObject:
    """Pretend to be an query response"""

    def __init__(self):
        self.sid = "AAAAA"


class MockedSQLBase:
    """Pretend to be a sql model"""

    # pylint: disable=C0103
    # pylint: disable=R0201
    def __init__(self):
        self.id = 0

    def create_all(self):
        """Mock the create_all method"""
        return

    def Column(self, obj, primary_key=True):
        """Mock the Column method"""
        return None

    def String(self, obj):
        """Mock the String method"""
        return None


class MockedDBParkRecord:
    """
    mocking the actual park record
    return from DB calls
    """

    def __init__(self, park_id):
        """
        initialize some db columns value
        """
        self.park_id = park_id


class MockedDBUserInformationRecord:
    """
    mocking the user information record
    return from DB calls
    """

    def __init__(self, weather_input):
        """
        initialize some db columns value
        """
        self.weather_input = weather_input


class MockedAllFunction:
    """
    Mocked All method of sql query
    """

    def __init__(self, park_id):
        """
        initialize some db columns value
        """
        self.park_id = park_id

    def all(self):
        """
        Mocked all method that returns all the records
        """
        return [MockedDBParkRecord(self.park_id)]

    def first(self):
        """
        mocking method first that returns park record
        """
        if self.park_id == "12":
            return "weather input"
        elif self.park_id == "1":
            return ""
        elif self.park_id == "1111":
            return MockedDBUserInformationRecord(self.park_id)
        else:
            return MockedDBParkRecord(self.park_id)

    def update(self, update_value):
        """Mocked update query"""
        return self.park_id


class MockedFavoriteParkQuery:
    """
    Mocking sql query that gets all the records from
    favorite_parks table
    """

    def __init__(self, email, login_type, park_id):
        """
        initialize some db columns value
        """
        self.email = email
        self.login_type = login_type
        self.park_id = park_id

    def filter_by(self, **kwarg):
        """
        Mocking filter_by method that
        returns all the records form db
        """
        return MockedAllFunction(self.park_id)


class MockedPersonalTabFirst:
    """Mock a false retrieval from the db"""
    def __init__(self):
        pass

    def first(self):
        """When a db call is done, return false"""
        return False

    def update(self, personal_values):
        """When a db update is done, return false"""
        return False


class MockedPersonalTab:
    """
    Mocking a personal tab retrieval
    """

    def __init__(self, email, login_type, personal_values):
        self.email = email
        self.login_type = login_type
        self.personal_values = personal_values

    def filter(self, email, login_type):
        """
        Return the mocked tab in order
        to simulate a false retrieval
        from the db
        """
        return MockedPersonalTabFirst()


# pylint: disable=R0902
# pylint: disable=R0916
# pylint: disable=R0201
# pylint: disable=R0912
# pylint: disable=R0904
class AppTestCases(unittest.TestCase):
    """Make all the test cases"""

    # pylint: disable=W0622
    # pylint: disable=R0913

    maxDiff = None

    def setUp(self):
        """Set up test cases"""
        self.success_test_params = []

    def mocked_flask_render(self, url):
        """Mock Flask render"""
        if not isinstance(url, str):
            raise ValueError("URL not string")

    def mock_do_nothing(self, first="", checkfirst="", bind=""):
        """Mock Session commit"""
        return

    def mock_get_latest_tweet(self):
        """Mock getting the latest tweets from politicians"""
        return {
            "gov": [
                {
                    "text": "A",
                    "sname": "A",
                    "ppic": "A",
                    "uname": "A",
                    "time": "A",
                    "date": "A",
                }
            ],
            "sen": [
                {
                    "text": "A",
                    "sname": "A",
                    "ppic": "A",
                    "uname": "A",
                    "time": "A",
                    "date": "A",
                },
                {
                    "text": "A",
                    "sname": "A",
                    "ppic": "A",
                    "uname": "A",
                    "time": "A",
                    "date": "A",
                },
            ],
        }

    def mock_get_latest_news(self):
        """Mock getting the latest news"""
        return [
            {
                "title": "A",
                "description": "A",
                "content": "A",
                "url": "A",
                "image": "A",
                "publishedAt": "A",
                "source": {"name": "A", "url": "A"},
            },
            {
                "title": "A",
                "description": "A",
                "content": "A",
                "url": "A",
                "image": "A",
                "publishedAt": "A",
                "source": {"name": "A", "url": "A"},
            },
        ]

    def mock_search_bills(
        self, sort, type, chamber, state, search_window, updated_since
    ):
        """Mock searching bills through openstates"""
        return [
            {
                "title": "Bill1",
                "updated_at": datetime.now(),
                "sponsors": [{"name": "Joe"}, {"name": "Sam"}],
                "actions": [{"action": "first"}, {"action": "second"}],
            },
            {
                "title": "Bill2",
                "updated_at": datetime.now(),
                "sponsors": [{"name": "Kat"}, {"name": "Nicole"}],
                "actions": [{"action": "first"}, {"action": "second"}],
            },
        ]

    def mock_search_politicians(self, state, chamber, active):
        """Pretend to search for politicians"""
        return [
            {
                "full_name": "Jake Blake",
                "photo_url": "aurlforjake",
                "url": "https://www.google.com/googling",
                "district": "76B",
                "party": "Libertarian",
                "chamber": "executive",
            },
            {
                "full_name": "Sam Schmidt",
                "photo_url": "samurl",
                "url": "https://www.google.com/saaaaaaammmmee",
                "district": "99",
                "party": "Republican",
                "chamber": "upper",
            },
        ]

    def mock_json_load_oldcache_bills(self, file):
        """Mock an outdated cache"""
        old_time = datetime.now().timestamp() - (50000 + 100)
        return {"timestamp": old_time}

    def mock_json_load_oldcache_politicians(self, file):
        """Mock an outdated cache"""
        old_time = datetime.now().timestamp() - (90000 + 100)
        return {"timestamp": old_time}

    def mock_session_query(self, model):
        """Mock Session commit"""
        return MockedQueryResponse(
            {"text": "TEST", "name": "USER", "time": datetime.now()}
        )

    def mock_session_first(self):
        """Mock getting a theme object"""
        return MockedThemeObj("color", "white")

    def mock_session_add_comment(self, comment):
        """Mock Session add for comments"""
        if not isinstance(comment.tab, str):
            raise ValueError("Tab not string")
        if not isinstance(comment.text, str):
            raise ValueError("Text not string")

    def mock_session_add_like(self, like):
        """Mock Session add for comments"""
        if not isinstance(like.email, str):
            raise ValueError("Email not string")
        if not isinstance(like.login_type, str):
            raise ValueError("Login type not string")
        if not isinstance(like.comment_id, int):
            raise ValueError("Comment ID not int")

    def mock_flask_emit_all(self, channel, data=""):
        """Mock Session add for comments"""
        if channel == "theme":
            if "pattern" not in data or not isinstance(data["pattern"], str):
                raise ValueError("NO PATTERN")
            if "value" not in data or not isinstance(data["value"], str):
                raise ValueError("NO VALUE")
        elif channel == "new comment":
            if "text" not in data or not isinstance(data["text"], str):
                raise ValueError("NO TEXT")
            if "tab" not in data or not isinstance(data["tab"], str):
                raise ValueError("NO TAB")
        elif channel == "liked comments":
            pass
        elif channel == "national parks update":
            pass
        elif channel == "update existing personal":
            pass
        else:
            raise ValueError("NO ESTABLISHED CHANNEL")

    def mock_flask_emit_one(self, channel, data=""):
        """Mock Session add for comments"""
        if channel == "old comments":
            if "comments" not in data:
                raise ValueError("NO COMMENTS")
            for comment in data["comments"]:
                if "text" not in comment:
                    raise ValueError("NO TEXT IN COMMENT")
        elif channel == "news":
            for news in data:
                if (
                    "title" not in news
                    or "description" not in news
                    or "content" not in news
                    or "url" not in news
                    or "image" not in news
                    or "publishedAt" not in news
                    or "source" not in news
                    or "name" not in news["source"]
                    or "url" not in news["source"]
                ):
                    raise ValueError
        elif channel == "political tweets":
            if "gov" not in data:
                raise ValueError("NO GOVENOR")
            for tweet in data["gov"]:
                if (
                    "text" not in tweet
                    or "sname" not in tweet
                    or "ppic" not in tweet
                    or "uname" not in tweet
                    or "time" not in tweet
                    or "date" not in tweet
                ):
                    raise ValueError
            if "sen" not in data:
                raise ValueError("NO SENATORS")
            for tweet in data["sen"]:
                if (
                    "text" not in tweet
                    or "sname" not in tweet
                    or "ppic" not in tweet
                    or "uname" not in tweet
                    or "time" not in tweet
                    or "date" not in tweet
                ):
                    raise ValueError
        elif channel == "send bills":
            for bill in data["bills"]:
                if (
                    "title" not in bill
                    or "updated_at" not in bill
                    or "sponsors" not in bill
                    or "last_action" not in bill
                ):
                    raise ValueError("VALUE MISSING IN BILL")
                for sponsor in bill["sponsors"]:
                    if not isinstance(sponsor, str):
                        raise ValueError("NAME BAD")
        elif channel == "send politicians":
            for pol in data["politicians"]:
                if (
                    "name" not in pol
                    or "photo" not in pol
                    or "website" not in pol
                    or "district" not in pol
                    or "party" not in pol
                    or "chamber" not in pol
                ):
                    raise ValueError("VALUE MISSING IN POLITICIAN")
        elif channel == "liked comments":
            for comment in data["comments"]:
                if not isinstance(comment, int):
                    raise ValueError("COMMENT ID IS NOT INT")
        elif channel == "send sport":
            pass
        elif channel == "national parks update":
            pass
        elif channel == "update existing personal":
            pass
        else:
            raise ValueError("NO ESTABLISHED CHANNEL")

    # pylint: disable=W0102
    def mock_flask_emit_weather(self, channel, data={}):
        """Mock Session for no emit (weather testing)"""
        if channel == "send weather":
            if len(data) == 0:
                raise ValueError("DATA IS EMPTY")
        elif channel in ("weather error", "update personal tab", "location_update"):
            pass
        else:
            raise ValueError("NO ESTABLISHED CHANNEL")

    def mock_sqlalchemy_create_engine(self, url):
        """Mock create_engine"""
        return "THIS IS AN ENGINE"

    def mock_html_unescape(self, escapable):
        """Mock html.unescape"""
        return "ESCAPED"

    def test_app_runs_success(self):
        """Test successful test cases"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ):
            import app

            with mock.patch("flask.render_template", self.mocked_flask_render):
                app.home()
            with mock.patch("flask.render_template", self.mocked_flask_render):
                app.commuter_tab()
            with mock.patch("flask.render_template", self.mocked_flask_render):
                app.politics_tab()
            with mock.patch("flask.render_template", self.mocked_flask_render):
                app.recreation_tab()
            with mock.patch("flask.render_template", self.mocked_flask_render):
                app.personal_tab()

    def test_app_new_comment(self):
        """Test successful new comments"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.commit", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.add", self.mock_session_add_comment
        ), mock.patch(
            "sqlalchemy.orm.Query.first", self.mock_session_first
        ), mock.patch(
            "flask_socketio.SocketIO.emit", self.mock_flask_emit_all
        ), mock.patch(
            "sqlalchemy.orm.session.Session.query", self.mock_session_query
        ), mock.patch(
            "flask_socketio.emit", self.mock_flask_emit_one
        ), mock.patch(
            "app.on_national_parks"
        ), mock.patch(
            "app.get_last_weather_input"
        ):

            mocker = mock.MagicMock()
            mocker.values("AAAA")
            with mock.patch("app.flask.request", mocker), mock.patch(
                "sqlalchemy.ext.declarative.declarative_base", mocker
            ):
                import app

                data = {
                    "newName": "Albert Einstein",
                    "newEmail": "einstein@mit.edu",
                    "loginType": "Google",
                }
                app.on_user_login(data)
                app.on_new_comment(
                    {"text": "Hello, I'm Joe", "name": "Joe", "tab": "Home"}
                )
                app.on_new_comment({"text": "Hello, I'm Joe"})
                app.on_new_comment({"text": 9, "tab": "Home"})
                app.on_new_comment({"text": "Hello", "tab": 7})
                app.on_new_comment({"text": "Hello, I'm Joe", "name": 9, "tab": "Home"})
                app.on_user_disconnect()
                app.on_new_comment(
                    {"text": "Hello, I'm Joe", "name": "Joe", "tab": "Home"}
                )

    def test_app_get_comments_success(self):
        """Test successful new comments"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.commit", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.add", self.mock_session_add_comment
        ), mock.patch(
            "flask_socketio.SocketIO.emit", self.mock_flask_emit_all
        ), mock.patch(
            "sqlalchemy.orm.session.Session.query", self.mock_session_query
        ), mock.patch(
            "flask_socketio.emit", self.mock_flask_emit_one
        ), mock.patch(
            "app.on_national_parks"
        ), mock.patch(
            "app.get_last_weather_input"
        ):
            mocker = mock.MagicMock()
            mocker.values("AAAA")
            with mock.patch("app.flask.request", mocker), mock.patch(
                "sqlalchemy.ext.declarative.declarative_base", mocker
            ):
                import app

                app.on_get_comments({"tab": "Home"})

                data = {
                    "newName": "Albert Einstein",
                    "newEmail": "einstein@mit.edu",
                    "loginType": "Google",
                }
                app.on_user_login(data)
                app.on_get_comments({"tab": "Home"})

    def test_app_like_comments(self):
        """Test successful like comments"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.commit", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.add", self.mock_session_add_like
        ), mock.patch(
            "flask_socketio.SocketIO.emit", self.mock_flask_emit_all
        ), mock.patch(
            "sqlalchemy.orm.session.Session.query", self.mock_session_query
        ), mock.patch(
            "flask_socketio.emit", self.mock_flask_emit_one
        ), mock.patch(
            "app.on_national_parks"
        ), mock.patch(
            "app.get_last_weather_input"
        ):

            mocker = mock.MagicMock()
            mocker.values("AAAA")
            with mock.patch("app.flask.request", mocker), mock.patch(
                "sqlalchemy.ext.declarative.declarative_base", mocker
            ):
                import app

                app.on_like_comment({"comment_id": 7, "like": False})

                data = {
                    "newName": "Joe",
                    "newEmail": "joseph@mit.edu",
                    "loginType": "Facebook",
                }
                app.on_user_login(data)
                app.on_like_comment({"comment_id": 8, "like": True})
                app.on_like_comment({"comment_id": 7, "like": False})
                app.on_like_comment({"comment_id": 8, "likes": True})
                app.on_user_disconnect()

    def test_app_get_comments_failure(self):
        """Test successful new comments"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.commit", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.add", self.mock_session_add_comment
        ), mock.patch(
            "flask_socketio.SocketIO.emit", self.mock_flask_emit_all
        ), mock.patch(
            "sqlalchemy.orm.session.Session.query", self.mock_session_query
        ), mock.patch(
            "flask_socketio.emit", self.mock_flask_emit_one
        ):
            mocker = mock.MagicMock()
            mocker.values("AAAA")
            session_mocker = mock.MagicMock()
            with mock.patch("app.flask.request", mocker), mock.patch(
                "sqlalchemy.orm.sessionmaker", session_mocker
            ):
                import app

                app.on_get_comments({})
                app.on_get_comments({"t": "Home"})

    def test_city_name_weather_sending(self):
        """test the on_weather_request function"""
        test_weather = {"city_name": "Newark"}
        import app

        with mock.patch("flask_socketio.emit", self.mock_flask_emit_weather):
            app.on_weather_request(test_weather)
            self.assertIsInstance(test_weather, dict)

    def test_zip_code_weather_sending(self):
        """test a zip code as the input"""
        test_weather = {"city_name": "07871"}
        import app

        with mock.patch("flask_socketio.emit", self.mock_flask_emit_weather):
            app.on_weather_request(test_weather)
            self.assertIsInstance(test_weather, dict)

    def test_invalid_code_weather_sending(self):
        """test an invalid, non NJ city"""
        test_weather = {"city_name": "Los Angeles"}
        import app

        with mock.patch("flask_socketio.emit", self.mock_flask_emit_weather):
            app.on_weather_request(test_weather)
            self.assertIsInstance(test_weather, dict)

    def test_render_landing_page(self):
        """Test landing_page rendering"""
        import app

        with mock.patch("flask.render_template", self.mocked_flask_render):
            app.landing_page()

    def test_on_pol_tweet_request(self):
        """test the on_pol_tweet_request function"""
        with mock.patch(
            "tweets.get_politicians_latest_tweets", self.mock_get_latest_tweet
        ):
            import app

            with mock.patch("flask_socketio.emit", self.mock_flask_emit_one):
                app.on_pol_tweet_request()

    def test_on_news_request(self):
        """test the on_news_request"""
        with mock.patch("news.get_latest_news", self.mock_get_latest_news):
            import app

            with mock.patch("flask_socketio.emit", self.mock_flask_emit_one):
                app.on_news_request()

    def test_get_sport_data(self):
        """Test the logic of get_sport_data function"""
        import app

        with mock.patch("flask_socketio.emit", self.mock_flask_emit_one):
            app.get_sport_data()

    def test_on_bill_request(self):
        """Test the on_bills_request method"""
        with mock.patch("json.load", self.mock_json_load_oldcache_bills), mock.patch(
            "pyopenstates.search_bills", self.mock_search_bills
        ), mock.patch("builtins.open", mock.mock_open()):
            import app

            with mock.patch("flask_socketio.emit", self.mock_flask_emit_one):
                app.on_bills_request()

    def test_on_politicians_request(self):
        """Test the on_politicians_request method"""
        with mock.patch(
            "json.load", self.mock_json_load_oldcache_politicians
        ), mock.patch(
            "pyopenstates.search_legislators", self.mock_search_politicians
        ), mock.patch(
            "builtins.open", mock.mock_open()
        ):
            import app

            with mock.patch("flask_socketio.emit", self.mock_flask_emit_one):
                app.on_politicians_request()

    def test_on_national_park(self):
        """Test the on_nationl_parks method that emits back all the parks to requested client"""
        import app

        with mock.patch("flask_socketio.emit") as mocked_socket_emit, mock.patch(
            "app.national_parks"
        ) as mocked_national_parks, mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            mocker = mock.MagicMock()
            mocker.sid = "12345"
            with mock.patch("app.flask.request", mocker):
                mocked_national_parks.return_value = [{"id": "12345"}]
                mocked_session_query.return_value = MockedFavoriteParkQuery(
                    "akashpatel@gmail.com", "Google", "12345"
                )
                app.LOGGEDIN_CLIENTS = {
                    "12345": {
                        "newEmail": "akashpatel@gmail.com",
                        "loginType": "Google",
                    },
                }
                app.on_national_parks()
                mocked_socket_emit.assert_called()

    def test_on_add_favorite_parks(self):
        """
        Test adding and removing park id to global variable LOGGEDIN_CLIENTS that either
        move from others to favorites or move from favorites to others
        """
        import app

        with mock.patch("app.SESSION.add") as mocked_session_add, mock.patch(
            "app.SESSION.delete"
        ) as mocked_session_delete, mock.patch("app.SESSION.commit"), mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            mocker = mock.MagicMock()
            mocker.sid = "12345"
            with mock.patch("app.flask.request", mocker):
                mocked_session_query.return_value = MockedFavoriteParkQuery(
                    "akashpatel@gmail.com", "Google", "12345"
                )

                data = {"parkID": "1234"}
                app.LOGGEDIN_CLIENTS = {
                    "12345": {"newEmail": "akashpatel@gmail.com", "loginType": "Google"}
                }
                app.on_add_favorite_parks(data)
                mocked_session_add.assert_called_once()

                data = {"parkID": "12345"}
                app.on_add_favorite_parks(data)
                mocked_session_delete.assert_called_once()

    def test_on_personal_tab_change(self):
        """Test the personal tab socket"""
        test_tabs = {"tab": "tested"}
        import app

        with mock.patch("app.SESSION.add") as mocked_session_add, mock.patch(
            "app.SESSION.delete"
        ) as mocked_session_delete, mock.patch("app.SESSION.commit"), mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            mocker = mock.MagicMock()
            mocker.sid = "12345"
            with mock.patch("app.flask.request", mocker):
                # pylint: disable=C0103
                LOGGEDIN_CLIENTS = {}
                LOGGEDIN_CLIENTS["12345"] = {"test": "done"}
                with mock.patch("flask_socketio.emit", self.mock_flask_emit_weather):
                    app.on_personal_tab_change(test_tabs)
                    self.assertIsInstance(test_tabs, dict)

    def test_on_personal_tab_change_failed(self):
        """Test the personal tab socket"""
        test_tabs = {"tab": "tested"}
        import app

        with mock.patch("app.SESSION.add") as mocked_session_add, mock.patch(
            "app.SESSION.delete"
        ) as mocked_session_delete, mock.patch("app.SESSION.commit"), mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            mocker = mock.MagicMock()
            mocker.sid = "12345"
            with mock.patch("app.flask.request", mocker):
                # pylint: disable=C0103
                LOGGEDIN_CLIENTS = {}
                LOGGEDIN_CLIENTS["12345"] = {"test": "done"}
                mocked_session_query.return_value = MockedPersonalTab(
                    "ameer", "fb", "test:true"
                )
                with mock.patch("flask_socketio.emit", self.mock_flask_emit_weather):
                    app.on_personal_tab_change(test_tabs)
                    self.assertIsInstance(test_tabs, dict)

    def mock_update_theme(self, data):
        """Mock Session update for theme"""
        if not isinstance(data["pattern"], str):
            raise ValueError("Pattern not string")
        if not isinstance(data["value"], str):
            raise ValueError("Value not string")

    def test_on_update_theme(self):
        """Test successful update theme"""
        with mock.patch("sqlalchemy.orm.Query.update", self.mock_update_theme):
            import app

            data = {
                "name": "Albert Einstein",
                "email": "einstein@mit.edu",
                "loginType": "Google",
                "pattern": "color",
                "value": "blue",
            }
            app.on_update_theme(data)

    def mock_session_add_theme(self, theme):
        """Mock Session add for themes"""
        if not isinstance(theme.name, str):
            raise ValueError("Name not string")
        if not isinstance(theme.email, str):
            raise ValueError("Email not string")
        if not isinstance(theme.login_type, str):
            raise ValueError("LoginType not string")
        if not isinstance(theme.pattern, str):
            raise ValueError("Pattern not string")
        if not isinstance(theme.value, str):
            raise ValueError("Value not string")

    def mock_session_first_failed(self):
        """Missing Doc String"""
        return None

    def mock_session_list_all(self):
        """Missing Doc String"""
        return [MockedQueryResponseObj("TEST", "USER", datetime.now())]

    def test_on_user_login(self):
        """Test successful login"""
        with mock.patch(
            "sqlalchemy.create_engine", self.mock_sqlalchemy_create_engine
        ), mock.patch(
            "sqlalchemy.sql.schema.MetaData.create_all", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.session.Session.commit", self.mock_do_nothing
        ), mock.patch(
            "sqlalchemy.orm.Query.first", self.mock_session_first_failed
        ), mock.patch(
            "sqlalchemy.orm.session.Session.add", self.mock_session_add_theme
        ), mock.patch(
            "flask_socketio.SocketIO.emit", self.mock_flask_emit_all
        ), mock.patch(
            "sqlalchemy.orm.Query.all", self.mock_session_list_all
        ), mock.patch(
            "flask_socketio.emit", self.mock_flask_emit_one
        ), mock.patch(
            "app.on_national_parks"
        ), mock.patch(
            "app.get_last_weather_input"
        ):
            mocker = mock.MagicMock()
            mocker.values("AAAA")
            with mock.patch("app.flask.request", mocker), mock.patch(
                "sqlalchemy.ext.declarative.declarative_base", mocker
            ):
                import app

                data = {
                    "newName": "Albert Einstein",
                    "newEmail": "einstein@mit.edu",
                    "loginType": "Google",
                }
                app.on_user_login(data)

    def test_on_last_weather_input(self):
        """
        Test function that either adds or updates t
        he last last searched weather
        """
        import app

        mocker = mock.MagicMock()
        mocker.sid = "12345"
        with mock.patch("app.flask.request", mocker), mock.patch(
            "app.SESSION.add"
        ) as mocked_session_add, mock.patch(
            "app.SESSION.commit"
        ) as mocked_session_commit, mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            data = {"last_weather_input": "jersey city"}
            mocked_session_query.return_value = MockedFavoriteParkQuery(
                "akashpatel@gmail.com", "Google", "12"
            )
            app.LOGGEDIN_CLIENTS = {
                "12345": {"newEmail": "akashpatel@gmail.com", "loginType": "Google"}
            }
            app.on_last_weather_input(data)
            mocked_session_commit.assert_called_once()

            mocked_session_query.return_value = MockedFavoriteParkQuery(
                "akashpatel@gmail.com", "Google", "1"
            )
            app.on_last_weather_input(data)

    def test_get_last_weather_input(self):
        """
        Test function that returns last
        user inputed city that stored in
        database or just return that they
        send in the request back
        """
        import app

        mocker = mock.MagicMock()
        mocker.sid = "12345"
        with mock.patch("app.flask.request", mocker), mock.patch(
            "app.on_weather_request"
        ), mock.patch("flask_socketio.emit") as mocked_socket_emit, mock.patch(
            "app.SESSION.query"
        ) as mocked_session_query:
            data = {"localStorage": "jersey city"}
            mocked_session_query.return_value = MockedFavoriteParkQuery(
                "akashpatel@gmail.com", "Google", "1111"
            )
            app.LOGGEDIN_CLIENTS = {
                "12345": {"newEmail": "akashpatel@gmail.com", "loginType": "Google"}
            }
            app.get_last_weather_input(data)

            mocked_socket_emit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
