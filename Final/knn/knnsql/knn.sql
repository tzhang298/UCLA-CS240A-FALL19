-- hint: shuffle
create table TESTDATA(PID integer, COLUMNNO integer, ATT float, DECISION integer);
create table TRAINDATA(PID integer, COLUMNNO integer, ATT float,DECISION integer);
create table TESTLAB(PID integer, LABEL integer);

WITH SQUARES(TESTID,TRAINID,SQ) AS
(SELECT S.PID, R.PID, POWER(R.ATT-S.ATT,2)
FROM TRAINDATA R, TESTDATA S
WHERE R.COLUMNNO = S.COLUMNNO),

DISTANCES(TESTID,TRAINID,DIST) AS
(SELECT TESTID, TRAINID, SUM(SQ)
FROM SQUARES
GROUP BY TESTID,TRAINID),

TOP5(TESTID, TRAINID) AS
	(SELECT T.TESTID,T.TRAINID
		FROM (SELECT TESTID,TRAINID,RANK() OVER (PARTITION BY TESTID ORDER BY DIST) AS RANK
						FROM DISTANCES)
		T WHERE RANK<=5
),

TOPDECISIONS(TESTID, TRAINID, DECISION) AS
(SELECT DISTINCT TESTID, TRAINID, DECISION
	FROM TOP5 T1,TRAINDATA T2
	WHERE T1.TRAINID=T2.PID),

MAJORITY(TESTID,CTR,PREDICTED) AS
(SELECT TESTID, COUNT(DECISION), DECISION
FROM TOPDECISIONS
GROUP BY TESTID,DECISION),

PREDICTION(TESTID, PREDICTED) AS
(SELECT TESTID,PREDICTED
	FROM (SELECT *,RANK() OVER (PARTITION BY TESTID ORDER BY CTR DESC) RNK FROM MAJORITY)
	WHERE RNK=1)

create view TEST_RESULTS(ROWNO,ACTUAL,PREDICTED) AS
(SELECT TESTID, LABEL, PREDICTED
		FROM PREDICTION,TESTLAB
		WHERE TESTID=PID)

WITH SUCCESS(NUM) AS
	(SELECT COUNT(PREDICTED) FROM TEST_RESULTS WHERE PREDICTED = ACTUAL),
TOTAL(NUM) AS
	(SELECT COUNT(PREDICTED) FROM TEST_RESULTS)

create view COMBINED_RESULTS(ACCURACY) AS
(SELECT CAST(SUCCESS.num AS DECIMAL(10,0))/CAST(TOTAL.num AS DECIMAL(10,0))
	FROM SUCCESS, TOTAL)

SELECT ACCURACY FROM COMBINED_RESULTS
