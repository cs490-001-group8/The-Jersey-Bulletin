import React, { useEffect, useState } from 'react';
import { Item, Placeholder, Image } from 'semantic-ui-react';
import axios from 'axios';
import WidgetTitle from './WidgetTitle';

const apiURL = 'https://gnews.io/api/v4/search?q=new jersey&max=10&token=';

export default function NewsList() {
  const [news, setNews] = useState(() => [{}, {}, {}, {}, {}]);
  const [loading, setLoading] = useState(() => true);

  useEffect(() => {
    axios.get(`${apiURL}${process.env.REACT_APP_NEWS_API_KEY}`).then((response) => {
      setNews(response.data.articles.slice(0, 5));
      setLoading(false);
    });
  });

  return (
    <div className="widget">
      <WidgetTitle title="News" />
      <Item.Group className="news-group">
        {news.map((item, index) => (
          <Item className="news-wrapper" key={index}>
            <Item.Image size="tiny" className="news-image">
              {loading ? (
                <Placeholder className="news-image">
                  <Placeholder.Image />
                </Placeholder>
              ) : (
                <Image src={item.image} className="news-image" />

              )}
            </Item.Image>
            <Item.Content>
              {loading ? (
                <Placeholder fluid>
                  <Placeholder.Header>
                    <Placeholder.Line />
                  </Placeholder.Header>
                  <Placeholder.Paragraph>
                    <Placeholder.Line />
                    <Placeholder.Line />
                    <Placeholder.Line />
                    <Placeholder.Line />
                  </Placeholder.Paragraph>
                </Placeholder>
              ) : (
                <>
                  <Item.Header as="a" href={item.url}>{item.title}</Item.Header>
                  <Item.Description className="news-description">{item.description}</Item.Description>
                </>
              )}
            </Item.Content>
          </Item>
        ))}
      </Item.Group>
    </div>
  );
}