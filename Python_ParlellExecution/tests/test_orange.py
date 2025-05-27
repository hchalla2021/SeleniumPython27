def test_facebook_edge(edge_driver):
    edge_driver.get("https://www.facebook.com/")
    assert "Facebook – log in or sign up" in edge_driver.title
