import pandas as pd

def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    def function(points1, points2):
        area = abs(points1["x_value"] - points2["x_value"])*abs(points1["y_value"] - points2["y_value"])
        if area > 0 and points1["id"] < points2["id"]:
            return [points1["id"], points2["id"], area]
        return None
    result = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            points1, points2 = points.iloc[i], points.iloc[j]
            data = function(points1, points2)
            if not data: continue
            result.append(data)
    # Convert the result list into a DataFrame
    df = pd.DataFrame(result, columns=["p1", "p2", "area"]).sort_values(["area", "p1", "p2"], ascending=[False, True, True])
    return df
