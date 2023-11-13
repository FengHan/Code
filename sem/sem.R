library(lavaan)
library(semPlot)

# 模拟数据生成
set.seed(123) # 确保结果可复现
N <- 200 # 样本大小
work_conditions <- rnorm(N, mean=5, sd=1.5)
salary_satisfaction <- rnorm(N, mean=5, sd=1.5)
colleague_relationships <- rnorm(N, mean=5, sd=1.5)
performance_assessment <- rnorm(N, mean=5, sd=1.5) + 0.3 * work_conditions
target_achievement <- rnorm(N, mean=5, sd=1.5) + 0.3 * salary_satisfaction
work_environment_items <- rnorm(N, mean=5, sd=1.5)
personal_motivation_items <- rnorm(N, mean=5, sd=1.5)

data <- data.frame(work_conditions, salary_satisfaction, colleague_relationships,
                   performance_assessment, target_achievement,
                   work_environment_items, personal_motivation_items)

# 定义SEM模型
model <- '
  # 测量模型
  JobSatisfaction =~ work_conditions + salary_satisfaction + colleague_relationships
  EmployeePerformance =~ performance_assessment + target_achievement
  WorkEnvironment =~ work_environment_items
  PersonalMotivation =~ personal_motivation_items

  # 结构模型
  EmployeePerformance ~ JobSatisfaction
  JobSatisfaction ~ WorkEnvironment + PersonalMotivation
'

# 拟合模型
fit <- sem(model, data = data)

# 绘制模型
# 绘制模型（假设 'fit' 是拟合好的模型）
semPaths(fit, whatLabels="est", layout="tree", rotation=2)

