process:

1.) form renders
2.) calculates using defaults automatically [POST: /calculate]
3.) hash_id automatically generated and saves results to redis
4.) template rendered and passed id
5.) template uses jquery and hash_id to call hash_id/results to get results and populate table [GET: results/<hash_id>]
6.) jquery listens for changes to inputs. Calls [UPDATE: /calculte/<hash_id>] if something changes