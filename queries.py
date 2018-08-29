query_1 = ''' SELECT title, slug, COUNT(*) from articles
              INNER JOIN log ON log.path LIKE CONCAT('%', articles.slug, '%')
              GROUP BY articles.title, articles.slug
              ORDER BY count DESC
              LIMIT 3 '''


query_2 = '''
            SELECT  name, sum(count) from 
                (SELECT title,slug, author, COUNT(*) from articles
                INNER JOIN log ON log.path LIKE CONCAT('%', articles.slug, '%')
                GROUP BY articles.title, articles.slug, articles.author) as views
            FULL JOIN authors on authors.id = author
            GROUP BY authors.name
            ORDER BY sum DESC
        '''


query_3 = '''
            SELECT date from
            ( SELECT date_trunc as date, sum(count) as total_views, sum(CASE
                                            WHEN status != '200 OK'
                                            THEN count
                                            else 0
                                            END) as error_count from
                ( SELECT date_trunc('day', time), status, COUNT(*) from log
                    GROUP BY date_trunc('day', time), log.status
                    ORDER BY date_trunc, status ) as logs
            GROUP BY date_trunc )  as counts
            WHERE (error_count / total_views) * 100 > 1
        '''
